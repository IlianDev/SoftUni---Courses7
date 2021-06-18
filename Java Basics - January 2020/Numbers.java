import java.util.Scanner;

public class Numbers {
    public static void main(String[] args) {
        Scanner scannner = new Scanner(System.in);
        String input = scannner.nextLine(); //"6
        int a = Integer.parseInt(input); //'6
        int area = a * a; // 36
        System.out.println(area); // ще си разпечатаме 36

    }
}
