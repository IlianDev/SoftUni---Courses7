import java.util.Scanner;

public class CharityCompany {
    public static void main(String[] args) {
        Scanner scanner = new Scanner (System.in);
        int days = Integer.parseInt(scanner.nextLine());
        int numCooker = Integer.parseInt(scanner.nextLine());
        int numCakes = Integer.parseInt(scanner.nextLine());
        int numGofreta =  Integer.parseInt(scanner.nextLine());
        int numPancakes = Integer.parseInt(scanner.nextLine());

        int totalCakes = numCakes*45;
        double totalGofreta = numGofreta*5.80;
        double totalPancakes = numPancakes*3.20;

        double totalSumPerDay = (totalCakes+totalGofreta+totalPancakes) * numCooker;
        double totalSumWholeCampany = totalSumPerDay * days;
        double expenses = totalSumWholeCampany * 0.125;
        double finalProfit = totalSumWholeCampany-expenses;

        System.out.printf("%.2f", finalProfit);

    }
}
