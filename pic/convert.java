import java.io.*;
import java.awt.image.*;
import javax.imageio.ImageIO;
import java.util.Arrays;
class convert {
    public static void main(String args[]) {
        if (args.length == 0) {
            System.err.println("Please supply image path.");
            System.exit(1);
        }
        for(String path: args) {
            try{
                convert(path);
            }catch (Exception ex) {
                System.err.println("Cannot convert " + path + ": "+ ex.getMessage());
            }
        }
    }
    public static void convert(String path) throws IOException {
        // open image
        File imgPath = new File(path);
        BufferedImage bufferedImage = ImageIO.read(imgPath);
        FileWriter write = new FileWriter(path.substring(0, path.lastIndexOf(".")));
        // get DataBufferBytes from Raster
        WritableRaster raster = bufferedImage .getRaster();
        DataBufferByte data   = (DataBufferByte) raster.getDataBuffer();

        byte[] bs = data.getData() ;
        int w = bufferedImage.getWidth(), h = bufferedImage.getHeight();
        StringBuilder sb = new StringBuilder();
        //sb.append(w + " "+ h);
        for (int i = 0; i < bs.length; i+=3) {
            sb.append(String.format(//"%02X%02X%02X"
            "%d,%d,%d", ((int)bs[i+2] + 256) % 256, ((int)bs[i+1] + 256) % 256, ((int)bs[i] + 256) % 256));
            if (i % (w * 3) == ((w-1) * 3)) sb.append("\n"); else sb.append(";");
        }
        write.append(sb.toString());
        write.close();
    }

}
