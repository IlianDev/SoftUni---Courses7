import java.util.Scanner;

public class NUmberEx {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = Integer.parseInt(scanner.nextLine());

        if (a>5 && a<10 && a%2==0){
            System.out.println("true");
        }else{
            System.out.println("false");
        }
    }
}
