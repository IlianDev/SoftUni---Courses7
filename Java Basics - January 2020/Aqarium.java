import java.util.Scanner;

public class Aqarium {
    public static void main(String[] args) {
        Scanner scannner = new Scanner(System.in);
        int lenght = Integer.parseInt(scannner.nextLine());
        int wide = Integer.parseInt(scannner.nextLine());
        int height = Integer.parseInt(scannner.nextLine());
        double persent = Double.parseDouble(scannner.nextLine());

        // сега намираме обема, now we will find the volume

        double liter = (lenght * wide * height)/1000.0; // обаче това ни е сантиметри. искаме да го превърнем в литри.
        double stuff = liter * persent/ 100;
        double totalLitres = liter - stuff;
        System.out.printf("%.3f", totalLitres);


        }

    }

//1.	Дължина в см – цяло число в интервала [10 … 500]
//2.	Широчина в см – цяло число в интервала [10 … 300]
//3.	Височина в см – цяло число в интервала [10… 200]
//4.	Процент  – реално число в интервала [0.000 … 100.000]