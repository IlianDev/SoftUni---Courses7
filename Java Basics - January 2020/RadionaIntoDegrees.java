import java.util.Scanner;

public class RadionaIntoDegrees {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double radians = Double.parseDouble(scanner.nextLine());
        double gradus = radians * 180/Math.PI;

        System.out.printf( "%.0f",gradus);



    }
}
