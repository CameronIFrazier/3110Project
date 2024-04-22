import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class NFANumericLiteralChecker {
    // Define states
    private enum State {
        START, STATE_1, STATE_2, STATE_3, STATE_4, STATE_5, STATE_6, STATE_7, INVALID
    }

    // Define transition table
    private static final Map<State, Map<Character, State>> transitionTable = new HashMap<>();

    static {
        // Start state transitions
        transitionTable.put(State.START, createStateMap('-', State.STATE_1, '0', State.STATE_3, '1', State.STATE_5, 'b', State.STATE_7));

        // State 1 transitions (negative sign)
        transitionTable.put(State.STATE_1, createStateMap('0', State.STATE_3, '1', State.STATE_5, 'b', State.STATE_7));

        // State 2 transitions (octal without leading zero)
        Map<Character, State> state2Transitions = createStateMap('1', State.STATE_2, '2', State.STATE_2, '3', State.STATE_2, '4', State.STATE_2, '5', State.STATE_2, '6', State.STATE_2, '7', State.STATE_2);
        transitionTable.put(State.STATE_2, state2Transitions);

        // State 3 transitions (octal with leading zero)
        Map<Character, State> state3Transitions = createStateMap('0', State.STATE_2, '1', State.STATE_2, '2', State.STATE_2, '3', State.STATE_2, '4', State.STATE_2, '5', State.STATE_2, '6', State.STATE_2, '7', State.STATE_2, 'o', State.STATE_4, 'O', State.STATE_4, 'x', State.STATE_6, 'X', State.STATE_6, '_', State.STATE_7);
        transitionTable.put(State.STATE_3, state3Transitions);

        // State 4 transitions (octal)
        transitionTable.put(State.STATE_4, state2Transitions);

        // State 5 transitions (decimal)
        Map<Character, State> state5Transitions = createStateMap('0', State.STATE_5, '1', State.STATE_5, '2', State.STATE_5, '3', State.STATE_5, '4', State.STATE_5, '5', State.STATE_5, '6', State.STATE_5, '7', State.STATE_5, '8', State.STATE_5, '9', State.STATE_5, '_', State.STATE_7);
        transitionTable.put(State.STATE_5, state5Transitions);

        // State 6 transitions (hexadecimal)
        Map<Character, State> state6Transitions = createStateMap('0', State.STATE_6, '1', State.STATE_6, '2', State.STATE_6, '3', State.STATE_6, '4', State.STATE_6, '5', State.STATE_6, '6', State.STATE_6, '7', State.STATE_6, '8', State.STATE_6, '9', State.STATE_6, 'a', State.STATE_6, 'b', State.STATE_6, 'c', State.STATE_6, 'd', State.STATE_6, 'e', State.STATE_6, 'f', State.STATE_6, 'A', State.STATE_6, 'B', State.STATE_6, 'C', State.STATE_6, 'D', State.STATE_6, 'E', State.STATE_6, 'F', State.STATE_6, '_', State.STATE_7);
        transitionTable.put(State.STATE_6, state6Transitions);

        // State 7 transitions (underscore)
        Map<Character, State> state7Transitions = createStateMap('0', State.STATE_7, '1', State.STATE_7, '2', State.STATE_7, '3', State.STATE_7, '4', State.STATE_7, '5', State.STATE_7, '6', State.STATE_7, '7', State.STATE_7, '8', State.STATE_7, '9', State.STATE_7, 'a', State.STATE_7, 'b', State.STATE_7, 'c', State.STATE_7, 'd', State.STATE_7, 'e', State.STATE_7, 'f', State.STATE_7, 'A', State.STATE_7, 'B', State.STATE_7, 'C', State.STATE_7, 'D', State.STATE_7, 'E', State.STATE_7, 'F', State.STATE_7, '_', State.STATE_7);
        transitionTable.put(State.STATE_7, state7Transitions);
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
            Map<Character, State> transitions = transitionTable.get(currentState);
            if (transitions == null || !transitions.containsKey(c)) {
                return false;
            }
            currentState = transitions.get(c);
        }
        return currentState == State.STATE_2 || currentState == State.STATE_4
                || currentState == State.STATE_5 || currentState == State.STATE_6
                || currentState == State.STATE_7;
    }

    // Method to get the type of integer (hexadecimal, octal, decimal)
    private static String getIntegerType(String input) {
        if (input.startsWith("0x") || input.startsWith("0X")) {
            return "Hexadecimal";
        } else if (input.startsWith("0")) {
            return "Octal";
        } else if (input.startsWith("0b") || input.startsWith("0B")) {
            return "Binary";
        } else {
            return "Decimal";
        }
    }

    // Helper method to create transitions map
    private static Map<Character, State> createStateMap(Object... args) {
        if (args.length % 2 != 0) {
            throw new IllegalArgumentException("Invalid number of arguments");
        }
        Map<Character, State> map = new HashMap<>();
        for (int i = 0; i < args.length; i += 2) {
            if (!(args[i] instanceof Character) || !(args[i + 1] instanceof State)) {
                throw new IllegalArgumentException("Invalid argument type");
            }
            map.put((Character) args[i], (State) args[i + 1]);
        }
        return map;
    }
}
