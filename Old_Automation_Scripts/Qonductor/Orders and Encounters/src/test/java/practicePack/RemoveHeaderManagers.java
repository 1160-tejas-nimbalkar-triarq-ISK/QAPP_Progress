package practicePack;
import java.io.File;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.transform.OutputKeys;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;

import org.w3c.dom.Document;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

public class RemoveHeaderManagers {

    public static void main(String[] args) {
        try {
            String jmxFilePath = "C:\\Users\\shraddha.rakshe\\Downloads\\Qoops_Client_Dashboard_Staging (1).jmx"; // Replace with the path to your JMeter .jmx file
            removeHeaderManagers(jmxFilePath);
            
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void removeHeaderManagers(String jmxFilePath) throws Exception {
        // Load and parse the .jmx file
        File jmxFile = new File(jmxFilePath);
        DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
        DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
        Document doc = dBuilder.parse(jmxFile);
        doc.getDocumentElement().normalize();

        // Find and remove all HeaderManager nodes
        NodeList headerManagers = doc.getElementsByTagName("HeaderManager");
        for (int i = 0; i < headerManagers.getLength(); i++) {
            Node headerManager = headerManagers.item(i);
            Node parent = headerManager.getParentNode();
            parent.removeChild(headerManager);
        }

        // Save the updated document back to the .jmx file
        TransformerFactory transformerFactory = TransformerFactory.newInstance();
        Transformer transformer = transformerFactory.newTransformer();
        transformer.setOutputProperty(OutputKeys.INDENT, "yes");
        DOMSource source = new DOMSource(doc);
        StreamResult result = new StreamResult(new File(jmxFilePath));
        transformer.transform(source, result);
    }
}
