import 'package:flutter/material.dart';

void showDialogSingleButton(BuildContext context, String title,
String message, String buttonLabel) {
  showDialog(
    context: context,
    builder: (BuildContext context) {
      // Return object of type Dialog
      return AlertDialog(
        title: new Text(title),
        content: new Text(message),
        actions: <Widget>[
          // usually buttons at the bottom of the dialog
          new FlatButton(
            onPressed: () {
              Navigator.of(context).pop();
            }, child: new Text(buttonLabel))
        ],
      );
    }
  );
}