import java.util.Scanner;
import java.util.WeakHashMap;

public class DancingRoom {
    public static void main(String[] args) {
        Scanner scanner = new Scanner (System.in);
        double L = Double.parseDouble(scanner.nextLine()); // dyljina zala
        double W = Double.parseDouble(scanner.nextLine()); // [irina zala
        double A = Double.parseDouble(scanner.nextLine()); // strana garderob

        double roomArea = (L*100) * (W*100); //golemina na zala v kv metri
        double chair = roomArea / 10; // golemina na pejka
        double wardropeArea = (A*100) *(A*100);
        double freeArea = roomArea- chair -wardropeArea;
        double freeSpaceDancers = freeArea/(40+7000);

        System.out.printf("%.0f", Math.floor(freeSpaceDancers));




    }
}
