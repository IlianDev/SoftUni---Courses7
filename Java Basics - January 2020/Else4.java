import java.util.Scanner;

public class Else4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int num = Integer.parseInt(scanner.nextLine());

        if (num == 1){
            System.out.println("one");
        }else if (num == 2){
            System.out.println("two");
        }else if (num > 3){
            System.out.println("Too little p");
        }
    }
}
