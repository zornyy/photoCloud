/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const collection = new Collection({
    "id": "ibh0o9bqtysuny9",
    "created": "2024-05-17 20:25:55.414Z",
    "updated": "2024-05-17 20:25:55.414Z",
    "name": "pictures",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "qnzfxoqe",
        "name": "field",
        "type": "relation",
        "required": true,
        "presentable": false,
        "unique": false,
        "options": {
          "collectionId": "_pb_users_auth_",
          "cascadeDelete": false,
          "minSelect": null,
          "maxSelect": 1,
          "displayFields": null
        }
      },
      {
        "system": false,
        "id": "mrxqxprt",
        "name": "field2",
        "type": "file",
        "required": true,
        "presentable": false,
        "unique": false,
        "options": {
          "mimeTypes": [
            "image/png",
            "image/vnd.mozilla.apng",
            "image/jpeg",
            "image/gif",
            "audio/mp4",
            "image/webp",
            "video/webm"
          ],
          "thumbs": [],
          "maxSelect": 1,
          "maxSize": 5242880,
          "protected": false
        }
      }
    ],
    "indexes": [],
    "listRule": null,
    "viewRule": null,
    "createRule": null,
    "updateRule": null,
    "deleteRule": null,
    "options": {}
  });

  return Dao(db).saveCollection(collection);
}, (db) => {
  const dao = new Dao(db);
  const collection = dao.findCollectionByNameOrId("ibh0o9bqtysuny9");

  return dao.deleteCollection(collection);
})
