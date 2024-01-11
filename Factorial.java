import java.math.BigInteger;
import java.math.*;

class Factorial{
    public static void main(String[] args){
        BigInteger number = new BigInteger("1");
        int fact = 25;

         for(Integer i = 1; i< fact+1; i++){

           number = number.multiply(new BigInteger(i.toString())); 

           //System.out.println(i + " " + number);
        }
        

        System.out.println((new BigInteger(number.toString())).divide(new BigInteger(10)));
    }
}