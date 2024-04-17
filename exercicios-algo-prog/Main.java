class Main {
    public static void main(String[] args) {
        
        Carro c1 = new Carro("Renaut","clio",2014,false);
        
        Carro c2 = new Carro(true);
        c2.setMarca("Fiat");
        c2.setModelo("Uno");
        c2.setAno(2019);
        
        System.out.println(c1.toString());
        System.out.println(c2.toString());
    }
}