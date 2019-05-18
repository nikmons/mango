import 'dart:async';
import 'package:flutter/material.dart';
import 'login_page.dart';

class SplashPage extends StatefulWidget {
  static String tag = 'splash-page';

  @override
  _SplashPageState createState() => _SplashPageState();
}

class _SplashPageState extends State<SplashPage> {
  final int splashDuration = 2;

  startTime() async {
    return Timer(
        Duration(seconds: splashDuration),
            () {
          //SystemChannels.textInput.invokeMethod('TextInput.hide');
          Navigator.of(context).pushReplacementNamed(LoginPage.tag);
        }
    );
  }

  @override
  void initState() {
    super.initState();
    startTime();
  }

  @override
  Widget build(BuildContext context) {
    var drawer = Drawer();

    return Scaffold(drawer: drawer,
        body: Container(
            decoration: BoxDecoration(color: Colors.white),
            child: Column(
              children: <Widget>[
                Expanded(child:
                Container(decoration: BoxDecoration(color: Colors.lightBlueAccent),
                  alignment: FractionalOffset(0.5, 0.3),
                  child:
                  Text("Mango - HR Management", style: TextStyle(fontSize: 40.0, color: Colors.white),),
                ),
                ),
                Container(margin: EdgeInsets.fromLTRB(0.0, 0.0, 0.0, 30.0),
                  child:
                  Text("© Copyright Statement 2019", style: TextStyle(fontSize: 16.0, color: Colors.lightBlueAccent,),
                  ),
                ),
              ],
            )
        )
    );
  }
}