using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Microsoft.Extensions.Logging;
using System.Threading.Tasks;  

namespace TestProject
{
    
    public class CSharpTest
    {
        private readonly ILogger logger;  
        public static string Connection_String;  
        private List<string> items = new();  

        
        public CSharpTest(ILogger logger) {
            this.logger = logger;  
        }

        
        public async Task<bool> ProcessItems()  
        {
            try {  
                var result = false;  
                
                if(items.Count == 0)  
                {
                    logger.LogWarning("No items to process");  
                    return result;
                }

                foreach(var item in items)  
                {
                    if (string.IsNullOrEmpty(item)) continue;  

                    
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
            catch(Exception ex)  
            {
                logger.LogError(ex, "Error processing items");  
                throw;  
            }
        }

        private async Task ProcessItem(string item)
        {
            
            await Task.Delay(1000);

            
            string upperItem = item.ToUpper();
            
            
            var length = upperItem.Length;

            switch(upperItem)  
            {
                case "A":
                    logger.LogInformation("Processing A");
                    break;
                case "B":
                    logger.LogInformation("Processing B");
                    break;
                default:  
                    logger.LogInformation("Processing unknown");
            }
        }

        
        public int Count 
        { 
            get { return items.Count; }  
            private set { }  
        }

        
        private void UnusedMethod()
        {
            Console.WriteLine("This method is never called");
        }
    }

    
    public interface IProcessor
    {
        Task<bool> Process();  
    }
} 
