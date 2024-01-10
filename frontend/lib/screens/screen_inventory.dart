import 'package:flutter/material.dart';
import 'package:frontend/models/inventory_model.dart';
import 'package:frontend/services/inventory_service.dart';
import 'package:frontend/widgets/inventory_widget.dart';

class InventoryScreen extends StatefulWidget {
  @override
  _InventoryScreenState createState() => _InventoryScreenState();
}

class _InventoryScreenState extends State<InventoryScreen> {
  late Future<List<InventoryModel>> futureInventories;

  @override
  void initState() {
    super.initState();
    futureInventories = InventoryService().fetchInventories();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Weapon List'),
      ),
      body: SizedBox(
        width: 250,
        child: FutureBuilder<List<InventoryModel>>(
          future: futureInventories,
          builder: (context, snapshot) {
            if (snapshot.connectionState == ConnectionState.waiting) {
              return Center(child: CircularProgressIndicator());
            } else if (snapshot.hasError) {
              return Center(child: Text('Error: ${snapshot.error}'));
            } else {
              return ListView.builder(
                itemCount: snapshot.data?.length ?? 0,
                itemBuilder: (context, index) {
                  return Container(
                    child: InventoryWidget(inventory: snapshot.data![index],),
                  );
                },
              );
            }
          },
        ),
      ),
    );
  }
}
