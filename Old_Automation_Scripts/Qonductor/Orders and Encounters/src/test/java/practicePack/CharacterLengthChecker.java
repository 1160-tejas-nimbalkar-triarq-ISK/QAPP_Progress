package practicePack;


public class CharacterLengthChecker {
    public static void main(String[] args) {
        // Sample string
        String myString = "This e-mail message and any documents attached to it are confidential and may contain information that is protected from This e-mail message and any documents attached to it are confidential and may contain information that is protected from qqqqqqqqqqqqq";
        String myString1 ="";
        // Check the character length
        int length = checkCharacterLength(myString);

        // Display the result
        System.out.println("Character Length: " + length);
    }

    // Function to check character length
    private static int checkCharacterLength(String input) {
        if (input != null) {
            return input.length();
        } else {
            return 0; // or handle null strings according to your requirements
        }
    }
}
