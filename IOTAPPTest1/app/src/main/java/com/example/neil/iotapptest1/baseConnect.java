package com.example.neil.iotapptest1;

import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class baseConnect extends AppCompatActivity {

    TextView output;
    EditText input;
    Button send;
    Intent i;
    String SERVER_IP;
    int SERVER_PORT;
    TcpClient mTcpClient;
    String error;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.test_layout);

        i = getIntent();
        SERVER_IP = i.getStringExtra("ip");
        SERVER_PORT = i.getIntExtra("port", 8888);
        Toast.makeText(getApplicationContext(), SERVER_IP + " : " + SERVER_PORT, Toast.LENGTH_SHORT).show();

        output = findViewById(R.id.output);
        input = findViewById(R.id.input);
        send = findViewById(R.id.send);

        new ConnectTask().execute("");

        if (mTcpClient != null) {
            mTcpClient.sendMessage("testing");
        }

    }


    public void sendClick(View v){
        if (!input.getText().toString().equals("")){
            if (mTcpClient != null) {
                mTcpClient.sendMessage(input.getText().toString()
                );
            }
        }

    }









    @Override
    protected void onDestroy() {
        super.onDestroy();
        if (mTcpClient != null) {
            mTcpClient.stopClient();
        }
    }


    public class ConnectTask extends AsyncTask<String, String, TcpClient> {

        @Override
        protected TcpClient doInBackground(String... message) {

            //we create a TCPClient object
            mTcpClient = new TcpClient(new TcpClient.OnMessageReceived() {
                @Override
                //here the messageReceived method is implemented
                public void messageReceived(String message) {
                    //this method calls the onProgressUpdate
                    publishProgress(message);
                }
            },SERVER_IP,SERVER_PORT,null);
            mTcpClient.run();

            return null;
        }

        @Override
        protected void onProgressUpdate(String... values) {
            super.onProgressUpdate(values);
            //response received from server
            Log.d("test", "response " + values[0]);
            //process server response here....

        }

    }
}
