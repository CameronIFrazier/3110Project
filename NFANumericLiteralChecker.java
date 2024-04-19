import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class NFANumericLiteralChecker {
    // Define states
    private enum State {
    START, STATE_1, STATE_2, STATE_3, STATE_4, STATE_5, STATE_6,
    STATE_7, INVALID
    }
    // Define transition table
    private static final Map<State, Map<Character, State>> transitionTable
    = new HashMap<>();
    static {
    // Start state transitions
    transitionTable.put(State.START, Map.of('-', State.STATE_1, '0',
    State.STATE_3, '1', State.STATE_5));
    // State 1 transitions (negative sign)
    transitionTable.put(State.STATE_1, Map.of('0', State.STATE_3, '1',
    State.STATE_5));
    // State 2 transitions (octal without leading zero)
    Map<Character, State> state2Transitions = new HashMap<>();
    for (char digit = '1'; digit <= '7'; digit++) {
    state2Transitions.put(digit, State.STATE_2);
    }
    transitionTable.put(State.STATE_2, state2Transitions);
    // State 3 transitions (octal with leading zero)
    Map<Character, State> state3Transitions = new HashMap<>();
    for (char digit = '0'; digit <= '7'; digit++) {
    state3Transitions.put(digit, State.STATE_2);
    }
    state3Transitions.put('o', State.STATE_4);
    state3Transitions.put('O', State.STATE_4);
    state3Transitions.put('x', State.STATE_6);
    state3Transitions.put('X', State.STATE_6);
    transitionTable.put(State.STATE_3, state3Transitions);
    // State 4 transitions (octal)
    transitionTable.put(State.STATE_4, state2Transitions);
    // State 5 transitions (decimal)
    Map<Character, State> state5Transitions = new HashMap<>();
    for (char digit = '0'; digit <= '9'; digit++) {
    state5Transitions.put(digit, State.STATE_5);
    }
    transitionTable.put(State.STATE_5, state5Transitions);
    // State 6 transitions (hexadecimal)
    Map<Character, State> state6Transitions = new HashMap<>();
    for (char digit = '0'; digit <= '9'; digit++) {
    state6Transitions.put(digit, State.STATE_6);
    }
    for (char letter = 'a'; letter <= 'f'; letter++) {
    state6Transitions.put(letter, State.STATE_6);
    }
    for (char letter = 'A'; letter <= 'F'; letter++) {
    state6Transitions.put(letter, State.STATE_6);
    }
    transitionTable.put(State.STATE_6, state6Transitions);
    }
    // Main method to check input
    public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.println("Enter an integer:");
    String input = scanner.nextLine().trim();
    if (isValidInteger(input)) {
    System.out.println(getIntegerType(input) + " integer: Valid.");
    } else {
    System.out.println("Invalid integer.");
    }
    }
    // Method to check if input is a valid integer
    private static boolean isValidInteger(String input) {
    State currentState = State.START;
    for (char c : input.toCharArray()) {
    Map<Character, State> transitions =
    transitionTable.get(currentState);
    if (transitions == null || !transitions.containsKey(c)) {
    return false;
    }
    currentState = transitions.get(c);
    }
    return currentState == State.STATE_2 || currentState ==
    State.STATE_4 || currentState == State.STATE_5 || currentState ==
    State.STATE_6;
    }
    // Method to get the type of integer (hexadecimal, octal, decimal)
    private static String getIntegerType(String input) {
    if (input.startsWith("0x") || input.startsWith("0X")) {
    return "Hexadecimal";
    } else if (input.startsWith("0")) {
    return "Octal";
    } else {
    return "Decimal";
    }
}
}