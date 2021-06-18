import java.util.Scanner;

public class MetricConvertor {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double value = Double.parseDouble(scanner.nextLine());
        String inputMetric = scanner.nextLine();
        String outputMetric = scanner.nextLine();

        if ("mm".equals(inputMetric)) {
            value = value/1000;
        }else if ("cm".equals(inputMetric)){
            value = value/100;
        }
        if ("mm".equals(outputMetric)){
            value = value*1000;
        }else if ("cm".equals(outputMetric)){
            value = value*100;
        }
        System.out.printf("%.3f", value);

    }
}
