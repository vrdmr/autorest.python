// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License. See License.txt in the project root for license information.

using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using AutoRest.Core;
using AutoRest.Core.Model;
using AutoRest.Core.Logging;
using AutoRest.Core.Utilities;
using AutoRest.Python;
using AutoRest.Python.Model;
using AutoRest.Python.vanilla.Templates;
using Newtonsoft.Json.Linq;

namespace AutoRest.Python
{
    public class CodeGeneratorPy : CodeGenerator
    {
        private const string ClientRuntimePackage = "msrest version 0.4.0";

        public CodeGeneratorPy()
        {
        }

        public override string UsageInstructions => $"The {ClientRuntimePackage} pip package is required to execute the generated code.";

        public override string ImplementationFileExtension => ".py";

        /// <summary>
        /// Generate Python client code for given ServiceClient.
        /// </summary>
        /// <param name="serviceClient"></param>
        /// <returns></returns>
        public override async Task Generate(CodeModel cm)
        {
            var codeModel = cm as CodeModelPy;
            if (codeModel == null)
            {
                throw new Exception("Code model is not a Python Code Model");
            }

            // Service client
            string[] namespaceParts = codeModel.Namespace.Split('.');
            for (int i = 1; i < namespaceParts.Length; ++i)
            {
                string initFolderName = Path.Combine(namespaceParts.Take(i).ToArray());
                await Write("__import__('pkg_resources').declare_namespace(__name__)",
                            Path.Combine(initFolderName, "__init__.py"), true);
            }

            var folderName = codeModel.Name.ToPythonCase().ToLower();
            var setupTemplate = new SetupTemplate { Model = codeModel };
            await Write(setupTemplate, "setup.py");

            var serviceClientInitTemplate = new ServiceClientInitTemplate { Model = codeModel };
            await Write(serviceClientInitTemplate, Path.Combine(folderName, "__init__.py"));

            var serviceClientTemplate = new ServiceClientTemplate { Model = codeModel };
            await Write(serviceClientTemplate, Path.Combine(folderName, codeModel.Name.ToPythonCase() + ".py"));

            var versionTemplate = new VersionTemplate { Model = codeModel };
            await Write(versionTemplate, Path.Combine(folderName, "version.py"));

            //Models
            if (codeModel.ModelTypes.Any())
            {
                var modelInitTemplate = new ModelInitTemplate { Model = codeModel };
                await Write(modelInitTemplate, Path.Combine(folderName, "models", "__init__.py"));

                foreach (var modelType in codeModel.ModelTemplateModels)
                {
                    var modelTemplate = new ModelTemplate
                    {
                        Model = modelType
                    };
                    await Write(modelTemplate, Path.Combine(folderName, "models", ((string)modelType.Name).ToPythonCase() + ".py"));
                }
            }

            //MethodGroups
            if (codeModel.MethodGroupModels.Any())
            {
                var methodGroupIndexTemplate = new MethodGroupInitTemplate
                {
                    Model = codeModel
                };
                await Write(methodGroupIndexTemplate, Path.Combine(folderName, "operations", "__init__.py"));

                foreach (var methodGroupModel in codeModel.MethodGroupModels)
                {
                    var methodGroupTemplate = new MethodGroupTemplate
                    {
                        Model = methodGroupModel
                    };
                    await Write(methodGroupTemplate, Path.Combine(folderName, "operations", ((string) methodGroupModel.TypeName).ToPythonCase() + ".py"));
                }
            }

            // Enums
            if (codeModel.EnumTypes.Any())
            {
                var enumTemplate = new EnumTemplate { Model = codeModel.EnumTypes };
                await Write(enumTemplate, Path.Combine(folderName, "models", codeModel.Name.ToPythonCase() + "_enums.py"));
            }
        }

        public static string BuildSummaryAndDescriptionString(string summary, string description)
        {
            StringBuilder builder = new StringBuilder();
            if (!string.IsNullOrEmpty(summary))
            {
                if (!summary.EndsWith(".", StringComparison.OrdinalIgnoreCase))
                {
                    summary += ".";
                }
                builder.AppendLine(summary);
            }

            if (!string.IsNullOrEmpty(summary) && !string.IsNullOrEmpty(description))
            {
                builder.AppendLine(TemplateConstants.EmptyLine);
            }

            if (!string.IsNullOrEmpty(description))
            {
                if (!description.EndsWith(".", StringComparison.OrdinalIgnoreCase))
                {
                    description += ".";
                }
                builder.Append(description);
            }

            return builder.ToString();
        }

       private string CreateObjectInitializer(CompositeType type, JObject obj, int indent = 0)
        {
            if (obj == null)
            {
                return "None";
            }

            var indentString = new string(' ', 4);
            var totalIndent = string.Concat(Enumerable.Repeat(indentString, indent));

            var properties = type.Properties.ToArray();

            var result = new StringBuilder();
            var propertyInitializers = new List<string>();
            foreach (var prop in properties)
            {
                var propValue = obj.SelectToken(prop.SerializedName);
                if (propValue != null)
                {
                    propertyInitializers.Add(totalIndent + indentString + $"{prop.Name} = {CreateInitializer(prop.ModelType, propValue, indent + 1)}");
                }
                else if (prop.IsRequired)
                {
                    Logger.Instance.Log(Category.Error, $"Required property '{prop.Name}' of type '{type.ClassName}' not found.");
                }
            }
            if (propertyInitializers.Count > 0)
            {
                // special treatment for SubResource
                if (type.ClassName.Split('.').Last() == "SubResource" && properties.Length == 1 && properties[0].SerializedName == "id")
                {
                    result.Append($"new {type.ClassName}({obj.SelectToken("id").ToString(Newtonsoft.Json.Formatting.None)})");
                }
                else
                {
                    result.AppendLine($"{type.ClassName}(");
                    result.AppendLine(string.Join(",\n", propertyInitializers));
                    result.Append(totalIndent + ")");
                }
            }
            else
            {
                result.Append($"new {type.ClassName}()");
            }
            return result.ToString();
        }

        private string CreateSequenceInitializer(SequenceType type, JArray arr, int indent = 0)
        {
            if (arr == null)
            {
                return "None";
            }

            var indentString = new string(' ', 4);
            var totalIndent = string.Concat(Enumerable.Repeat(indentString, indent));

            var result = new StringBuilder();
            var itemInitializer = new List<string>();
            foreach (var item in arr)
            {
                itemInitializer.Add(totalIndent + indentString + CreateInitializer(type.ElementType, item, indent + 1));
            }
            if (itemInitializer.Count > 0)
            {
                result.AppendLine("[");
                result.AppendLine(string.Join(",\n", itemInitializer));
                result.Append(totalIndent + "]");
            }
            else
            {
                result.Append("[]");
            }
            return result.ToString();
        }

        private string CreateInitializer(IModelType type, JToken token, int indent = 0)
            => type is CompositeType ct
            ? CreateObjectInitializer(ct, token as JObject, indent)
            : type is SequenceType st
            ? CreateSequenceInitializer(st, token as JArray, indent)
            : CodeNamer.Instance.EscapeDefaultValue(token.ToString(), type);

        public override string GenerateSample(bool isolateSnippet, CodeModel cm, MethodGroup g, Method m, string exampleName, AutoRest.Core.Model.XmsExtensions.Example example)
        {
            var clientInstanceName = "client";
            var codeModel = cm as CodeModelPy;
            var method = m as MethodPy;
            var group = g as MethodGroupPy;

            var result = new StringBuilder();
            if (isolateSnippet)
            {
                result.AppendLine("{");
                result.AppendLine("// Client: " + cm.Name);
                if (!g.Name.IsNullOrEmpty())
                {
                    result.AppendLine("// Group: " + g.Name);
                }
                result.AppendLine("// Method: " + m.Name);
                result.AppendLine("// Example: " + exampleName);
                result.AppendLine();
            }

            // parameter preparation
            var paramaters = new List<string>();
            var contiguous = false; // true;
            foreach (var formalParameter in method.LocalParameters)
            {
                // parameter found in x-ms-examples?
                if (example.Parameters.TryGetValue(formalParameter.SerializedName, out JToken token))
                {
                    var value = CreateInitializer(formalParameter.ModelType, token);
                    // initialize composite type beforehand
                    if (formalParameter.ModelType is CompositeType ct)
                    {
                        result.AppendLine($"{formalParameter.Name} = {value}");
                        value = formalParameter.Name;
                    }
                    paramaters.Add((contiguous ? "" : formalParameter.Name + " = ") + value);
                }
                else if (formalParameter.IsRequired) // ...but it should be there!
                {
                    Logger.Instance.Log(Category.Error, $"Required parameter '{formalParameter.SerializedName}' not found.");
                    return null;
                }
                else
                {
                    contiguous = false;
                }
            }
            result.AppendLine();

            // call
            var returnTypeName = method.ReturnType.Body?.Name ?? method.ReturnType.Headers?.Name;
            returnTypeName = returnTypeName?.ToCamelCase();

            result.AppendLine($"{(returnTypeName == null ? "" : $"{returnTypeName} = ")}{clientInstanceName}{(g.Name.IsNullOrEmpty() ? "" : "." + g.NameForProperty)}.{m.Name}(" +
                $"{string.Join(", ", paramaters.Select(param => "\n    " + param))}\n)");

            if (isolateSnippet)
            {
                result.AppendLine("}");
            }
            return result.ToString();
        }
    }    
}
