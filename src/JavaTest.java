import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Random;

/**
 * Java test file with intentional issues
 */
public class JavaTest {
    
    // Public non-final static field (not recommended)
    public static String GLOBAL_CONFIG = "config.json";
    
    // Inconsistent naming convention
    private int Counter;
    
    // Hardcoded credentials
    private static final String API_KEY = "1234567890abcdef";
    private static final String PASSWORD = "admin123";
    
    // Missing constructor
    
    /**
     * Process data with inefficient string concatenation
     */
    public List<String> processData(List<String> data) {
        List<String> result = new ArrayList<String>();
        for (String item : data) {
            // Inefficient string concatenation
            String output = "";
            for (int i = 0; i < item.length(); i++) {
                output = output + item.charAt(i);
            }
            result.add(output);
        }
        return result;
    }
    
    /**
     * Security issue: SQL injection vulnerability
     */
    public void executeQuery(String userInput) {
        String query = "SELECT * FROM users WHERE name = '" + userInput + "'";
        // Execute query without sanitizing input
        System.out.println("Executing: " + query);
    }
    
    /**
     * Resource leak: not closing reader
     */
    public String readFileWithLeak(String filename) {
        try {
            BufferedReader reader = new BufferedReader(new FileReader(filename));
            StringBuilder content = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                content.append(line);
            }
            // Missing reader.close()
            return content.toString();
        } catch (IOException e) {
            return null;
        }
    }
    
    /**
     * Inefficient collection usage
     */
    public boolean containsString(List<String> list, String target) {
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i).equals(target)) {
                return true;
            }
        }
        return false;
    }
    
    /**
     * Deprecated Date usage
     */
    public void processDate() {
        Date date = new Date();
        int year = date.getYear();  // Deprecated method
        System.out.println("Year: " + year);
    }
    
    /**
     * Potential null pointer exception
     */
    public void processNullable(String input) {
        if (input.length() > 5) {  // No null check before using input
            System.out.println("Input is long enough");
        }
    }
    
    /**
     * Unused parameter
     */
    public double calculateAverage(List<Double> numbers, int precision, String extraParam) {
        double total = 0;
        for (Double num : numbers) {
            total += num;
        }
        return total / numbers.size();
    }
    
    /**
     * Empty catch block
     */
    public void riskyOperation() {
        try {
            int result = 10 / 0;  // Will throw ArithmeticException
        } catch (Exception e) {
            // Empty catch block, error is swallowed
        }
    }
    
    /**
     * Main method with multiple issues
     */
    public static void main(String[] args) {
        // Magic number
        if (args.length > 3) {
            System.out.println("Too many arguments");
        }
        
        JavaTest test = new JavaTest();
        
        List<String> data = new ArrayList<>();
        data.add("item1");
        data.add("item2");
        data.add("item3");
        
        List<String> processed = test.processData(data);
        System.out.println(processed);
        
        // Potential division by zero
        Random random = new Random();
        int denominator = random.nextInt(2);  // 0 or 1
        int result = 100 / denominator;  // May cause ArithmeticException
        
        System.out.println("Done processing");
    }
} 
