import java.util.ArrayList;
import java.util.Comparator;

public class HW {
   public static void main(String[] args){
     Integer[] U32 = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19};
     Integer[] L3L =  U32;
     ArrayList <ArrayList<Integer>> groups = new ArrayList<>(U32.length);
     ArrayList<Integer> temp = new ArrayList<>();
     for(int j = 0; j<U32.length; j++){
        System.out.println("\na="+U32[j]);
         for(int i = 0; i<L3L.length;i++){
              temp.add((L3L[i]+U32[j])%20);
              System.out.print(temp.get(i) + ", ");
        
        
        groups.add(temp);
        temp.clear();
    }

 
   } 
}
}
