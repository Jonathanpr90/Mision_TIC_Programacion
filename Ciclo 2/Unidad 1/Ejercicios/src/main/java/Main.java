public class Main {
    public static void main(String[] args) {
        BecaUniversitaria becaUniversitaria = new BecaUniversitaria(48,1000,2.0);
        System.out.println(becaUniversitaria.calcularInteresSimple());
        System.out.println(becaUniversitaria.calcularInteresCompuesto());
        System.out.println(becaUniversitaria.compararInversion(0,0,0));
    }

}
