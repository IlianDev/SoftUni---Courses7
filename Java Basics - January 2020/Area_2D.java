import java.util.Scanner;

public class Area_2D {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double x1 =Double.parseDouble(scanner.nextLine());
        double y1 =Double.parseDouble(scanner.nextLine());
        double x2 =Double.parseDouble(scanner.nextLine());
        double y2 =Double.parseDouble(scanner.nextLine());

        double length = Math.abs(x1- x2);
        double width = Math.abs(y1- y2);

        double area = length*width; // лице на фигурата
        System.out.printf("%.2f", area);

        System.out.println();

        double parametyr = 2*(length+width);
        System.out.printf("%.2f", parametyr);


    }
}
