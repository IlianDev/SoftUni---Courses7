import java.util.Scanner;

public class AlcoholShop {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double whiskeyPrice = Double.parseDouble(scanner.nextLine());
        double beerQuantity = Double.parseDouble(scanner.nextLine());
        double wineQuantity = Double.parseDouble(scanner.nextLine());
        double rakiqQuantity = Double.parseDouble(scanner.nextLine());
        double whiskeyQuantity = Double.parseDouble(scanner.nextLine());

        double rakiqPrice = whiskeyPrice * 0.5; // tova e za 1 lityr
        double winePrice = rakiqPrice *0.6;
        double beerPrice = rakiqPrice *0.2;

        double totalPrice = (whiskeyPrice* whiskeyQuantity) +
                (beerPrice*beerQuantity) +
                (winePrice*wineQuantity) +
                (rakiqPrice*rakiqQuantity);
        System.out.printf("%.2f", totalPrice);

    }
}

