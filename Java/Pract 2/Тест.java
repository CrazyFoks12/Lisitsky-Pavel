import java.util.Scanner;

public class Тест {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = 3;
        int m = 3;
        int[][] matrix = new int[n][m];

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                matrix[i][j] = (int) ((Math.random()*20) - 10);
                System.out.print(matrix[i][j] + "\t");
            }
            System.out.println();
        }
        int i=2;
        int k=0;
        for (int j=0; j<matrix.length; j++) {
            if (matrix[i][j]>0) {
                k++;
            }
        }
        System.out.println("Element " + k);
        }
    }
