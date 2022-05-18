//Дан одномерный массив a(n) в котором находится единственный нулевой элемент. Найти где он находится, и упорядочить
//по возрастанию элементы, расположенные за ним. Выдать на экран номер элемента и упорядоченный массив.
import java.util.*;

public class Задание2 {
	   public static void main(String args[]) {
		int array[] = {5, 3, 7, 0, 8, 6, 11,};
		 int item = 0;
		      for(int i=0; i<array.length; i++) {
		         if (array[i] == item) {
		           System.out.println(item + " Located in " + (i+1));
		           Arrays.sort(array, i+1, array.length);
		         	}
		      }
	        for(int i = 0; i <  array.length; i++) {
	        System.out.print(array[i] + "  ");
	        }
	   }
}
