import java.util.Scanner;

public class ex {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String firstName = scan.nextLine(); // това ще ми прочете един ред
        String lastName = scan.nextLine();
        int age = Integer.parseInt (scan.nextLine());// това ще превърне в цяло число
        String town = scan.nextLine();

        System.out.printf ("You are %s %s, a %d-years old person, from %s.",
                firstName, lastName, age, town);





    }

    }

