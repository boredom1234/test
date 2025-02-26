using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Microsoft.Extensions.Logging;
using System.Threading.Tasks;  // Unordered usings (StyleCop)

namespace TestProject
{
    // Missing class documentation (StyleCop)
    public class CSharpTest
    {
        private readonly ILogger logger;  // Field missing underscore prefix (StyleCop)
        public static string Connection_String;  // Public field should be property (Roslyn)
        private List<string> items = new();  // Field should be readonly (ReSharper)

        // Constructor missing documentation (StyleCop)
        public CSharpTest(ILogger logger) {
            this.logger = logger;  // Unnecessary this (ReSharper)
        }

        // Method missing documentation (StyleCop)
        public async Task<bool> ProcessItems()  // Missing cancellation token (ReSharper)
        {
            try {  // Curly brace on same line (StyleCop)
                var result = false;  // Variable can be const (Roslyn)
                
                if(items.Count == 0)  // Missing space after if (StyleCop)
                {
                    logger.LogWarning("No items to process");  // String should be in constant (ReSharper)
                    return result;
                }

                foreach(var item in items)  // Missing space after foreach (StyleCop)
                {
                    if (string.IsNullOrEmpty(item)) continue;  // Should use braces (StyleCop)

                    // Nested conditional can be simplified (ReSharper)
                    if (item.Length > 0)
                    {
                        if (item[0] == 'A')
                        {
                            await ProcessItem(item);
                        }
                    }
                }

                return true;
            }
            catch(Exception ex)  // Missing space after catch (StyleCop)
            {
                logger.LogError(ex, "Error processing items");  // String should be in constant (ReSharper)
                throw;  // Should throw more specific exception (Roslyn)
            }
        }

        private async Task ProcessItem(string item)
        {
            // Magic number (ReSharper)
            await Task.Delay(1000);

            // Possible null reference (Roslyn)
            string upperItem = item.ToUpper();
            
            // Unused variable (Roslyn)
            var length = upperItem.Length;

            switch(upperItem)  // Missing space after switch (StyleCop)
            {
                case "A":
                    logger.LogInformation("Processing A");
                    break;
                case "B":
                    logger.LogInformation("Processing B");
                    break;
                default:  // Missing break (StyleCop)
                    logger.LogInformation("Processing unknown");
            }
        }

        // Property missing documentation (StyleCop)
        public int Count 
        { 
            get { return items.Count; }  // Expression body syntax preferred (Roslyn)
            private set { }  // Empty setter (ReSharper)
        }

        // Unused private method (ReSharper)
        private void UnusedMethod()
        {
            Console.WriteLine("This method is never called");
        }
    }

    // Missing interface documentation (StyleCop)
    public interface IProcessor
    {
        Task<bool> Process();  // Missing cancellation token (ReSharper)
    }
} 
