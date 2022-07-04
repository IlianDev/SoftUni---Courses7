import java.util.Scanner;

public class WorldSwimmingRecord {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double recordInSeconds = Double.parseDouble(scanner.nextLine());
        double distanceInMetres = Double.parseDouble(scanner.nextLine());
        double oneMetrePerSecond = Double.parseDouble(scanner.nextLine());

        double neededDistanceToSwim = distanceInMetres * oneMetrePerSecond;

        double minus15m = distanceInMetres/15;
        double minus15m2 = minus15m * 12.5;

        double totalTime = neededDistanceToSwim +minus15m2;

        if (totalTime > recordInSeconds){
            double diff = totalTime - recordInSeconds;
            System.out.printf("Yes, he succeeded! The new world record is %.2f seconds.", totalTime);
        }else {
            double diff2 = recordInSeconds - totalTime;
            System.out.printf("No, he failed! He was %.2f seconds slower.");
        }

    }
}
