public class BecaUniversitaria {

    private int pTiempo;
    private double pMonto;
    private double pInteres;

    public BecaUniversitaria(int pTiempo, double pMonto, double pInteres) {
        this.pTiempo = pTiempo;
        this.pMonto = pMonto;
        this.pInteres = pInteres;
    }
    public BecaUniversitaria() {
        this.pTiempo = 0;
        this.pMonto = 0.0;
        this.pInteres = 0.0;
    }
    public String compararInversion(int pTiempo, double pMonto, double pInteres) {
        this.pTiempo = pTiempo;
        this.pMonto = pMonto;
        this.pInteres = pInteres;
        double diferencia =calcularInteresCompuesto() - calcularInteresSimple();
        return "La diferencia entre la proyección de interés compuesto e interés simple es: $" + diferencia;
    }

    public String compararInversion() {
        if(pTiempo == 0 && pMonto == 0 && pInteres == 0){
            return "No se obtuvo diferencia entre las proyecciones, revisar los parámetros de entrada.";
        }else{
            double diferencia =calcularInteresCompuesto() - calcularInteresSimple();
            return "La diferencia entre la proyección de interés compuesto e interés simple es: $" + diferencia;
        }
    }

    public double calcularInteresSimple() {
        double interesSimple = pMonto * (pInteres / 100) * pTiempo;
        return Math.round(interesSimple);
    }

    public double calcularInteresCompuesto() {
        double interesCompuesto = pMonto * (Math.pow(1 + (pInteres / 100), pTiempo) - 1);
        return Math.round(interesCompuesto);
    }
}

