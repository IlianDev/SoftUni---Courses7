import java.util.Scanner;

public class YearsMsMrsMr {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int years =Integer.parseInt(scanner.nextLine());
        String gender = scanner.nextLine();

        if (gender.equals("f")){
            if (years<16){
                System.out.println("Miss");
            }else {
                System.out.println("Miss");
            }

        }else {
            if (years<16){
                System.out.println("Master");
            }else{
                System.out.println("Mr");
            }
        }

    }
}
