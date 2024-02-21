import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;

import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;

public class CircleArea implements HttpHandler {

    @Override
    public void handle(HttpExchange exchange) throws IOException {
        String radiusParam = exchange.getRequestURI().getQuery().split("=")[1];
        int radius;
        try {
            radius = Integer.parseInt(radiusParam);
        } catch (NumberFormatException e) {
            exchange.sendResponseHeaders(400, 0);
            return;
        }

        double area = calculateArea(radius);

        String response = "Java: " + String.format("%.2f", area);

        exchange.sendResponseHeaders(200, response.length());
        OutputStream os = exchange.getResponseBody();
        os.write(response.getBytes());
        os.close();
    }

    private double calculateArea(int radius) {
        return Math.PI * Math.pow(radius, 2);
    }

    public static void main(String[] args) throws IOException {
        HttpServer server = HttpServer.create(new InetSocketAddress(Integer.parseInt(System.getenv("JAVA_BACKEND_PORT"))), 0);
        server.createContext("/circle-area", new CircleArea());
        server.setExecutor(null);
        server.start();
    }
}