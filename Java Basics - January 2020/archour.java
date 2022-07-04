import java.util.Scanner;

public class archour {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String name = scan.nextLine();
        int projectCount = Integer.parseInt(scan.nextLine());
        int hours = projectCount*3;


        System.out.printf("The architect %s will need %d hours to complete %d project/s.",
                name,hours,projectCount);
    }
}
//Zadacha 5
//•	"The architect {името на архитекта} will need {необходими часове} hours to complete {брой на проектите} project/s."