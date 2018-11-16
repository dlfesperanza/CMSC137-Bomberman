import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.PrintStream;

class sendChat {
  // This function fills in a Person message based on user input.
 /*
  static TcpPacketProtos PromptForAChat(BufferedReader stdin,
                                 PrintStream stdout) throws IOException {
    TcpPacketProtos.Builder packet = TcpPacketProtos.newBuilder();

    stdout.print("Enter message: ");
    packet.setMessage(stdin.readLine());

    packet.setType(new PacketType(3))

    return person.build();
  }
*/
  static TcpPacketProtos CreateCreateLobbyPacket(){
    TcpPacketProtos.Builder packet = TcpPacketProtos.newBuilder();
    PacketType type = new PacketType(2);
    packet.settype(type);
    packet.setlobby_id(12345);
    return packet.build();
  }

  // Main function:  Reads the entire address book from a file,
  //   adds one person based on user input, then writes it back out to the same
  //   file.
  public static void main(String[] args) throws Exception {
    
    TcpPacketProtos.Builder lobbypacket = CreateCreateLobbyPacket();

    System.out.println(lobbypacket);
  }
}