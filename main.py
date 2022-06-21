#Updated_edited_text
#is _here
#is_it_shown?

#using_save
#is_here

package com.example.mobile_computing_assign;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import com.google.android.material.button.MaterialButton;

public class MainActivity extends AppCompatActivity {

    EditText username;
    EditText password;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        username =(EditText) findViewById(R.id.username);
        password =(EditText) findViewById(R.id.password);
        MaterialButton loginbutton =(MaterialButton) findViewById(R.id.loginbutton);
        TextView forgot = (TextView) findViewById(R.id.forgot);
        TextView noacc =(TextView) findViewById(R.id.noacc);


        loginbutton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                gotologin();
            }
        });

        forgot.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                passwordClick();
            }
        });

        noacc.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                registerClick();
            }
        });

    }
    private void gotologin(){
        String str= username.getText().toString();
        String str2= password.getText().toString();

        Intent intent = new Intent(this, LoginActivity.class);
        intent.putExtra("message_key", str);
        intent.putExtra("message_key2", str2);
        startActivity(intent);

    }

    public void passwordClick(){
        Intent intent = new Intent(this, PassActivity.class);
        startActivity(intent);
    }

    private void registerClick(){
        Intent intent = new Intent(this, RegisterActivity.class);
        startActivity(intent);
    }
}