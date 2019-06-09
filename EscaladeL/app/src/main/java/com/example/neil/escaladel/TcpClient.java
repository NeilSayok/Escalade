package com.example.neil.escaladel;

import android.support.design.widget.Snackbar;
import android.util.Log;
import android.view.View;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.InetAddress;
import java.net.Socket;

public class TcpClient {

    public static final String TAG = TcpClient.class.getSimpleName();
    public  String SERVER_IP; //server IP address
    public  int SERVER_PORT;;
    private String mServerMessage;  // message to send to the server
    private OnMessageReceived mMessageListener = null;  // sends message received notifications
    private boolean mRun = false;    // while this is true, the server will continue running

    private PrintWriter mBufferOut;    // used to send messages
    private BufferedReader mBufferIn;    // used to read messages from the server

    View v;

    public TcpClient(OnMessageReceived listener, String ip , int port, View ctx) {
        mMessageListener = listener;
        SERVER_IP = ip;
        SERVER_PORT = port;
        v = ctx;
    }

    public void sendMessage(final String message) {
        Runnable runnable = new Runnable() {
            @Override
            public void run() {
                if (mBufferOut != null) {
                    Log.d(TAG, "Sending: " + message);
                    mBufferOut.println(message);
                    mBufferOut.flush();
                }
            }
        };
        Thread thread = new Thread(runnable);
        thread.start();
    }

    public void stopClient() {
        mRun = false;
        if (mBufferOut != null) {
            mBufferOut.flush();
            mBufferOut.close();
        }
        mMessageListener = null;
        mBufferIn = null;
        mBufferOut = null;
        mServerMessage = null;
    }

    public void run() {
        mRun = true;
        try {
            //here you must put your computer's IP address.
            InetAddress serverAddr = InetAddress.getByName(SERVER_IP);
            Log.d("TCP Client", "C: Connecting...");
            //create a socket to make the connection with the server
            Socket socket = new Socket(serverAddr, SERVER_PORT);
            Snackbar.make(v,"Connected",Snackbar.LENGTH_LONG)
                    .setAction("Ok", new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                }
            }).show();

            try {
                //sends the message to the server
                mBufferOut = new PrintWriter(new BufferedWriter(new OutputStreamWriter(socket.getOutputStream())), true);
                //receives the message which the server sends back
                mBufferIn = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                while (mRun) {
                    mServerMessage = mBufferIn.readLine();
                    if (mServerMessage != null && mMessageListener != null) {
                        //call the method messageReceived from MyActivity class
                        mMessageListener.messageReceived(mServerMessage);
                    }

                }
                Log.d("RESPONSE FROM SERVER", "S: Received Message: '" + mServerMessage + "'");
            } catch (Exception e) {
                Log.e("TCP", "S: Error", e);
                //makeText(mCtx,e.toString(),Toast.LENGTH_SHORT).show();
                Snackbar.make(v,"Connection Failed",Snackbar.LENGTH_LONG).setAction("Ok", new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {
                    }
                }).show();
            } finally {
                socket.close();
            }

        } catch (Exception e) {
            Log.e("TCP", "C: Error", e);
            Snackbar.make(v,"Connection Failed",Snackbar.LENGTH_LONG).setAction("Ok", new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                }
            }).show();



        }

    }

    public interface OnMessageReceived {
        public void messageReceived(String message);
    }

}