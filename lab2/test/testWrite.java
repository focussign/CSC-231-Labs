import java.io.*;


class readAndWrite {
public static void main(String args[]) {
try {
File file = new File("thing.txt");
if(file.createNewFile()) {
System.out.println("File create");
} else{
System.out.println("Already exists");
}
} catch (IOException e) {
e.printStackTrace();
}

}


}
