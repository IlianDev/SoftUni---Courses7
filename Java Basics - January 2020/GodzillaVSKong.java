import java.util.Scanner;
import java.util.function.DoubleFunction;

public class GodzillaVSKong {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double budgetForMuvie = Double.parseDouble(scanner.nextLine());
        int numberOfStatists = Integer.parseInt(scanner.nextLine());
        double clothesFor1Statist = Double.parseDouble(scanner.nextLine());

        double dekor = budgetForMuvie*0.1;
        double clothesForAllStatists = numberOfStatists*clothesFor1Statist;

        if (numberOfStatists > 150){
            clothesForAllStatists = clothesForAllStatists*0.9;
        }
        double totalPriceFilm = dekor+clothesForAllStatists;
        if (totalPriceFilm > budgetForMuvie){
            System.out.println("Not enough money!");
            double diff = totalPriceFilm-budgetForMuvie;
            System.out.printf("Wingard needs %.2f leva more.", diff);
        }else{
            System.out.println("Action!");
            double diff2 = budgetForMuvie-totalPriceFilm;
            System.out.printf("Wingard starts filming with %.2f leva left.", diff2);

        }
    }
}
