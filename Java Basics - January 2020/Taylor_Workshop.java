import java.util.Scanner;

public class Taylor_Workshop {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int tables = Integer.parseInt(scanner.nextLine());   // broj masi
        double tableLength  = Double.parseDouble(scanner.nextLine());// dyljina na masi v metri
        double tableWidth  = Double.parseDouble(scanner.nextLine()); // shirina na masa

        double oneAreaCover =tables* (tableLength+2*0.3)*(tableWidth+2*0.3);

        double side = tableLength/2;
        double squareCoversCloth = side*side*tables;

        double priceUSd1 = oneAreaCover*7;
        double priceUSd2 = squareCoversCloth*9;
        double USDtotal = priceUSd1+priceUSd2;
        double LevTotal = USDtotal*1.85;
        System.out.printf("%.2f %n", USDtotal);
        System.out.printf("%.2f", LevTotal);

    }
}
