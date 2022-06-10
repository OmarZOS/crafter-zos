

import helma.xmlrpc.WebServer;
import java.util.Hashtable;

/**
 * Hello world!
 *
 */
public class Hasher 
{
    
     // This public method will be exposed to XML-RPC client
     public Hashtable sumAndDifference(int x, int y) {
        Hashtable result = new Hashtable();
        result.put("sum", new Integer(x + y));
        result.put("difference", new Integer(x - y));
        return result;
    }

    public void print() {
        System.out.println("Print Systems");
    }

    public static void main( String[] args ) {
        try {
            WebServer server = new WebServer(4213);
            // Our handler is a regular java object
            server.addHandler("handler", new Hasher());
        } catch (Exception exception) {
            System.err.println("JavaServer" + exception.toString());
        }
    }
}