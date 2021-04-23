package cs.mad.habittracker.entities;

import androidx.room.DatabaseConfiguration;
import androidx.room.InvalidationTracker;
import androidx.room.RoomOpenHelper;
import androidx.room.RoomOpenHelper.Delegate;
import androidx.room.RoomOpenHelper.ValidationResult;
import androidx.room.util.DBUtil;
import androidx.room.util.TableInfo;
import androidx.room.util.TableInfo.Column;
import androidx.room.util.TableInfo.ForeignKey;
import androidx.room.util.TableInfo.Index;
import androidx.sqlite.db.SupportSQLiteDatabase;
import androidx.sqlite.db.SupportSQLiteOpenHelper;
import androidx.sqlite.db.SupportSQLiteOpenHelper.Callback;
import androidx.sqlite.db.SupportSQLiteOpenHelper.Configuration;
import java.lang.Override;
import java.lang.String;
import java.lang.SuppressWarnings;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

@SuppressWarnings({"unchecked", "deprecation"})
public final class HabitDatabase_Impl extends HabitDatabase {
  private volatile HabitDao _habitDao;

  @Override
  protected SupportSQLiteOpenHelper createOpenHelper(DatabaseConfiguration configuration) {
    final SupportSQLiteOpenHelper.Callback _openCallback = new RoomOpenHelper(configuration, new RoomOpenHelper.Delegate(6) {
      @Override
      public void createAllTables(SupportSQLiteDatabase _db) {
        _db.execSQL("CREATE TABLE IF NOT EXISTS `Habit` (`myId` INTEGER PRIMARY KEY AUTOINCREMENT, `name` TEXT NOT NULL, `goal` INTEGER NOT NULL, `interval` TEXT NOT NULL, `timesPerformed` INTEGER NOT NULL, `date_created` INTEGER NOT NULL, `timerTime` TEXT NOT NULL, `timerInterval` TEXT NOT NULL, `reminderTime` TEXT NOT NULL, `notes` TEXT NOT NULL)");
        _db.execSQL("CREATE TABLE IF NOT EXISTS room_master_table (id INTEGER PRIMARY KEY,identity_hash TEXT)");
        _db.execSQL("INSERT OR REPLACE INTO room_master_table (id,identity_hash) VALUES(42, '1fa1a47adc3113523677909b211171e8')");
      }

      @Override
      public void dropAllTables(SupportSQLiteDatabase _db) {
        _db.execSQL("DROP TABLE IF EXISTS `Habit`");
        if (mCallbacks != null) {
          for (int _i = 0, _size = mCallbacks.size(); _i < _size; _i++) {
            mCallbacks.get(_i).onDestructiveMigration(_db);
          }
        }
      }

      @Override
      protected void onCreate(SupportSQLiteDatabase _db) {
        if (mCallbacks != null) {
          for (int _i = 0, _size = mCallbacks.size(); _i < _size; _i++) {
            mCallbacks.get(_i).onCreate(_db);
          }
        }
      }

      @Override
      public void onOpen(SupportSQLiteDatabase _db) {
        mDatabase = _db;
        internalInitInvalidationTracker(_db);
        if (mCallbacks != null) {
          for (int _i = 0, _size = mCallbacks.size(); _i < _size; _i++) {
            mCallbacks.get(_i).onOpen(_db);
          }
        }
      }

      @Override
      public void onPreMigrate(SupportSQLiteDatabase _db) {
        DBUtil.dropFtsSyncTriggers(_db);
      }

      @Override
      public void onPostMigrate(SupportSQLiteDatabase _db) {
      }

      @Override
      protected RoomOpenHelper.ValidationResult onValidateSchema(SupportSQLiteDatabase _db) {
        final HashMap<String, TableInfo.Column> _columnsHabit = new HashMap<String, TableInfo.Column>(10);
        _columnsHabit.put("myId", new TableInfo.Column("myId", "INTEGER", false, 1, null, TableInfo.CREATED_FROM_ENTITY));
        _columnsHabit.put("name", new TableInfo.Column("name", "TEXT", true, 0, null, TableInfo.CREATED_FROM_ENTITY));
        _columnsHabit.put("goal", new TableInfo.Column("goal", "INTEGER", true, 0, null, TableInfo.CREATED_FROM_ENTITY));
        _columnsHabit.put("interval", new TableInfo.Column("interval", "TEXT", true, 0, null, TableInfo.CREATED_FROM_ENTITY));
        _columnsHabit.put("timesPerformed", new TableInfo.Column("timesPerformed", "INTEGER", true, 0, null, TableInfo.CREATED_FROM_ENTITY));
        _columnsHabit.put("date_created", new TableInfo.Column("date_created", "INTEGER", true, 0, null, TableInfo.CREATED_FROM_ENTITY));
        _columnsHabit.put("timerTime", new TableInfo.Column("timerTime", "TEXT", true, 0, null, TableInfo.CREATED_FROM_ENTITY));
        _columnsHabit.put("timerInterval", new TableInfo.Column("timerInterval", "TEXT", true, 0, null, TableInfo.CREATED_FROM_ENTITY));
        _columnsHabit.put("reminderTime", new TableInfo.Column("reminderTime", "TEXT", true, 0, null, TableInfo.CREATED_FROM_ENTITY));
        _columnsHabit.put("notes", new TableInfo.Column("notes", "TEXT", true, 0, null, TableInfo.CREATED_FROM_ENTITY));
        final HashSet<TableInfo.ForeignKey> _foreignKeysHabit = new HashSet<TableInfo.ForeignKey>(0);
        final HashSet<TableInfo.Index> _indicesHabit = new HashSet<TableInfo.Index>(0);
        final TableInfo _infoHabit = new TableInfo("Habit", _columnsHabit, _foreignKeysHabit, _indicesHabit);
        final TableInfo _existingHabit = TableInfo.read(_db, "Habit");
        if (! _infoHabit.equals(_existingHabit)) {
          return new RoomOpenHelper.ValidationResult(false, "Habit(cs.mad.habittracker.entities.Habit).\n"
                  + " Expected:\n" + _infoHabit + "\n"
                  + " Found:\n" + _existingHabit);
        }
        return new RoomOpenHelper.ValidationResult(true, null);
      }
    }, "1fa1a47adc3113523677909b211171e8", "76d041543063d106911812dc29375851");
    final SupportSQLiteOpenHelper.Configuration _sqliteConfig = SupportSQLiteOpenHelper.Configuration.builder(configuration.context)
        .name(configuration.name)
        .callback(_openCallback)
        .build();
    final SupportSQLiteOpenHelper _helper = configuration.sqliteOpenHelperFactory.create(_sqliteConfig);
    return _helper;
  }

  @Override
  protected InvalidationTracker createInvalidationTracker() {
    final HashMap<String, String> _shadowTablesMap = new HashMap<String, String>(0);
    HashMap<String, Set<String>> _viewTables = new HashMap<String, Set<String>>(0);
    return new InvalidationTracker(this, _shadowTablesMap, _viewTables, "Habit");
  }

  @Override
  public void clearAllTables() {
    super.assertNotMainThread();
    final SupportSQLiteDatabase _db = super.getOpenHelper().getWritableDatabase();
    try {
      super.beginTransaction();
      _db.execSQL("DELETE FROM `Habit`");
      super.setTransactionSuccessful();
    } finally {
      super.endTransaction();
      _db.query("PRAGMA wal_checkpoint(FULL)").close();
      if (!_db.inTransaction()) {
        _db.execSQL("VACUUM");
      }
    }
  }

  @Override
  public HabitDao habitDao() {
    if (_habitDao != null) {
      return _habitDao;
    } else {
      synchronized(this) {
        if(_habitDao == null) {
          _habitDao = new HabitDao_Impl(this);
        }
        return _habitDao;
      }
    }
  }
}
