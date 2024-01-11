import java.lang.reflect.Array;
import java.util.ArrayList;

public class Cipher {
    public static void main(String[] args){
        ArrayList<Character> letters = new ArrayList<>();
        char[] listLetters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
        for(char a: listLetters){
            letters.add(a);
        }
        String key = args[1];
        key = key.toLowerCase();
        String phrase =args[0];
        phrase = phrase.toLowerCase();
        String output ="";
        int keyptr = 0;
        int letterAdd = 0;
        for(int i = 0; i < phrase.length(); i++){
            if(!((phrase.charAt(i) == (' ')) || 
                 (phrase.charAt(i) == (',')) ||
                 (phrase.charAt(i) == ('\'')))){
            letterAdd =(letters.indexOf(phrase.charAt(i)) - letters.indexOf(key.charAt(keyptr)));
            if(letterAdd < 0)
                letterAdd = letterAdd + 26;
            output += letters.get(letterAdd);
            if(keyptr == key.length()-1){
                keyptr = 0;
            }else{
                keyptr++;
            }
            }
        }

        System.out.println(output.toUpperCase());
    }
}
