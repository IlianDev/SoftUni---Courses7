import java.util.Scanner;

public class TimePlusFifteenMinutes {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int startHour = Integer.parseInt(scanner.nextLine());
        int startMinutes = Integer.parseInt(scanner.nextLine());

        int timeInMinutes = (startHour * 60) + startMinutes;
        int timePlus15 = timeInMinutes + 15;

        int finalHour = timePlus15/60;
        int finalMinutes = timeInMinutes%60;

        if (finalHour >= 24){
            finalHour = finalHour - 24;
        }
        if (finalHour < 10){
            System.out.printf("%d:0%d", finalHour,finalMinutes);
        }else{
            System.out.printf("%d: %d" ,finalHour,finalMinutes);
        }
    }
}
