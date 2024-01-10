class InventoryModel {
  final String ownerName;
  final List<dynamic> itemList;

  InventoryModel({
    required this.ownerName,
    required this.itemList,
  });

  factory InventoryModel.fromJson(Map<String, dynamic> json) {
    return InventoryModel(
      ownerName: json['소유캐릭터이름'],
      itemList: json['목록'] as List<dynamic>,
    );
  }
}