import 'package:flutter/material.dart';
import 'package:mango_flutter_app/ui/login_page.dart';
import 'package:mango_flutter_app/ui/home_page.dart';
import 'package:mango_flutter_app/ui/register_page.dart';
import 'package:mango_flutter_app/ui/splash_page.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  final routes = <String, WidgetBuilder>{
    LoginPage.tag: (context) => LoginPage(),
    HomePage.tag: (context) => HomePage(),
    RegisterPage.tag: (context) => RegisterPage(),
    SplashPage.tag: (context) => SplashPage()
  };

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Mango',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.lightBlue,
        fontFamily: 'Nunito',
      ),
      home: SplashPage(),
      routes: routes,
    );
  }
}
