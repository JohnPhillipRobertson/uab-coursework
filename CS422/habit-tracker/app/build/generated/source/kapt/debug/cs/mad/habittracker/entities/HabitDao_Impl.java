package cs.mad.habittracker.entities;

import android.database.Cursor;
import androidx.room.CoroutinesRoom;
import androidx.room.EntityDeletionOrUpdateAdapter;
import androidx.room.EntityInsertionAdapter;
import androidx.room.RoomDatabase;
import androidx.room.RoomSQLiteQuery;
import androidx.room.SharedSQLiteStatement;
import androidx.room.util.CursorUtil;
import androidx.room.util.DBUtil;
import androidx.sqlite.db.SupportSQLiteStatement;
import java.lang.Exception;
import java.lang.Long;
import java.lang.Object;
import java.lang.Override;
import java.lang.String;
import java.lang.SuppressWarnings;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.Callable;
import kotlin.Unit;
import kotlin.coroutines.Continuation;

@SuppressWarnings({"unchecked", "deprecation"})
public final class HabitDao_Impl implements HabitDao {
  private final RoomDatabase __db;

  private final EntityInsertionAdapter<Habit> __insertionAdapterOfHabit;

  private final EntityDeletionOrUpdateAdapter<Habit> __deletionAdapterOfHabit;

  private final EntityDeletionOrUpdateAdapter<Habit> __updateAdapterOfHabit;

  private final SharedSQLiteStatement __preparedStmtOfDeleteFromWeb;

  public HabitDao_Impl(RoomDatabase __db) {
    this.__db = __db;
    this.__insertionAdapterOfHabit = new EntityInsertionAdapter<Habit>(__db) {
      @Override
      public String createQuery() {
        return "INSERT OR ABORT INTO `Habit` (`myId`,`name`,`goal`,`interval`,`timesPerformed`,`date_created`,`timerTime`,`timerInterval`,`reminderTime`,`notes`) VALUES (?,?,?,?,?,?,?,?,?,?)";
      }

      @Override
      public void bind(SupportSQLiteStatement stmt, Habit value) {
        if (value.getMyId() == null) {
          stmt.bindNull(1);
        } else {
          stmt.bindLong(1, value.getMyId());
        }
        if (value.getName() == null) {
          stmt.bindNull(2);
        } else {
          stmt.bindString(2, value.getName());
        }
        stmt.bindLong(3, value.getGoal());
        if (value.getInterval() == null) {
          stmt.bindNull(4);
        } else {
          stmt.bindString(4, value.getInterval());
        }
        stmt.bindLong(5, value.getTimesPerformed());
        stmt.bindLong(6, value.getDate_created());
        if (value.getTimerTime() == null) {
          stmt.bindNull(7);
        } else {
          stmt.bindString(7, value.getTimerTime());
        }
        if (value.getTimerInterval() == null) {
          stmt.bindNull(8);
        } else {
          stmt.bindString(8, value.getTimerInterval());
        }
        if (value.getReminderTime() == null) {
          stmt.bindNull(9);
        } else {
          stmt.bindString(9, value.getReminderTime());
        }
        if (value.getNotes() == null) {
          stmt.bindNull(10);
        } else {
          stmt.bindString(10, value.getNotes());
        }
      }
    };
    this.__deletionAdapterOfHabit = new EntityDeletionOrUpdateAdapter<Habit>(__db) {
      @Override
      public String createQuery() {
        return "DELETE FROM `Habit` WHERE `myId` = ?";
      }

      @Override
      public void bind(SupportSQLiteStatement stmt, Habit value) {
        if (value.getMyId() == null) {
          stmt.bindNull(1);
        } else {
          stmt.bindLong(1, value.getMyId());
        }
      }
    };
    this.__updateAdapterOfHabit = new EntityDeletionOrUpdateAdapter<Habit>(__db) {
      @Override
      public String createQuery() {
        return "UPDATE OR ABORT `Habit` SET `myId` = ?,`name` = ?,`goal` = ?,`interval` = ?,`timesPerformed` = ?,`date_created` = ?,`timerTime` = ?,`timerInterval` = ?,`reminderTime` = ?,`notes` = ? WHERE `myId` = ?";
      }

      @Override
      public void bind(SupportSQLiteStatement stmt, Habit value) {
        if (value.getMyId() == null) {
          stmt.bindNull(1);
        } else {
          stmt.bindLong(1, value.getMyId());
        }
        if (value.getName() == null) {
          stmt.bindNull(2);
        } else {
          stmt.bindString(2, value.getName());
        }
        stmt.bindLong(3, value.getGoal());
        if (value.getInterval() == null) {
          stmt.bindNull(4);
        } else {
          stmt.bindString(4, value.getInterval());
        }
        stmt.bindLong(5, value.getTimesPerformed());
        stmt.bindLong(6, value.getDate_created());
        if (value.getTimerTime() == null) {
          stmt.bindNull(7);
        } else {
          stmt.bindString(7, value.getTimerTime());
        }
        if (value.getTimerInterval() == null) {
          stmt.bindNull(8);
        } else {
          stmt.bindString(8, value.getTimerInterval());
        }
        if (value.getReminderTime() == null) {
          stmt.bindNull(9);
        } else {
          stmt.bindString(9, value.getReminderTime());
        }
        if (value.getNotes() == null) {
          stmt.bindNull(10);
        } else {
          stmt.bindString(10, value.getNotes());
        }
        if (value.getMyId() == null) {
          stmt.bindNull(11);
        } else {
          stmt.bindLong(11, value.getMyId());
        }
      }
    };
    this.__preparedStmtOfDeleteFromWeb = new SharedSQLiteStatement(__db) {
      @Override
      public String createQuery() {
        final String _query = "DELETE FROM habit WHERE myID NOT NULL";
        return _query;
      }
    };
  }

  @Override
  public Object insert(final Habit[] habit, final Continuation<? super Unit> p1) {
    return CoroutinesRoom.execute(__db, true, new Callable<Unit>() {
      @Override
      public Unit call() throws Exception {
        __db.beginTransaction();
        try {
          __insertionAdapterOfHabit.insert(habit);
          __db.setTransactionSuccessful();
          return Unit.INSTANCE;
        } finally {
          __db.endTransaction();
        }
      }
    }, p1);
  }

  @Override
  public Object insert(final List<Habit> habits, final Continuation<? super Unit> p1) {
    return CoroutinesRoom.execute(__db, true, new Callable<Unit>() {
      @Override
      public Unit call() throws Exception {
        __db.beginTransaction();
        try {
          __insertionAdapterOfHabit.insert(habits);
          __db.setTransactionSuccessful();
          return Unit.INSTANCE;
        } finally {
          __db.endTransaction();
        }
      }
    }, p1);
  }

  @Override
  public Object delete(final Habit habit, final Continuation<? super Unit> p1) {
    return CoroutinesRoom.execute(__db, true, new Callable<Unit>() {
      @Override
      public Unit call() throws Exception {
        __db.beginTransaction();
        try {
          __deletionAdapterOfHabit.handle(habit);
          __db.setTransactionSuccessful();
          return Unit.INSTANCE;
        } finally {
          __db.endTransaction();
        }
      }
    }, p1);
  }

  @Override
  public Object update(final Habit habit, final Continuation<? super Unit> p1) {
    return CoroutinesRoom.execute(__db, true, new Callable<Unit>() {
      @Override
      public Unit call() throws Exception {
        __db.beginTransaction();
        try {
          __updateAdapterOfHabit.handle(habit);
          __db.setTransactionSuccessful();
          return Unit.INSTANCE;
        } finally {
          __db.endTransaction();
        }
      }
    }, p1);
  }

  @Override
  public Object deleteFromWeb(final Continuation<? super Unit> p0) {
    return CoroutinesRoom.execute(__db, true, new Callable<Unit>() {
      @Override
      public Unit call() throws Exception {
        final SupportSQLiteStatement _stmt = __preparedStmtOfDeleteFromWeb.acquire();
        __db.beginTransaction();
        try {
          _stmt.executeUpdateDelete();
          __db.setTransactionSuccessful();
          return Unit.INSTANCE;
        } finally {
          __db.endTransaction();
          __preparedStmtOfDeleteFromWeb.release(_stmt);
        }
      }
    }, p0);
  }

  @Override
  public Object getAll(final Continuation<? super List<Habit>> p0) {
    final String _sql = "SELECT * FROM habit";
    final RoomSQLiteQuery _statement = RoomSQLiteQuery.acquire(_sql, 0);
    return CoroutinesRoom.execute(__db, false, new Callable<List<Habit>>() {
      @Override
      public List<Habit> call() throws Exception {
        final Cursor _cursor = DBUtil.query(__db, _statement, false, null);
        try {
          final int _cursorIndexOfMyId = CursorUtil.getColumnIndexOrThrow(_cursor, "myId");
          final int _cursorIndexOfName = CursorUtil.getColumnIndexOrThrow(_cursor, "name");
          final int _cursorIndexOfGoal = CursorUtil.getColumnIndexOrThrow(_cursor, "goal");
          final int _cursorIndexOfInterval = CursorUtil.getColumnIndexOrThrow(_cursor, "interval");
          final int _cursorIndexOfTimesPerformed = CursorUtil.getColumnIndexOrThrow(_cursor, "timesPerformed");
          final int _cursorIndexOfDateCreated = CursorUtil.getColumnIndexOrThrow(_cursor, "date_created");
          final int _cursorIndexOfTimerTime = CursorUtil.getColumnIndexOrThrow(_cursor, "timerTime");
          final int _cursorIndexOfTimerInterval = CursorUtil.getColumnIndexOrThrow(_cursor, "timerInterval");
          final int _cursorIndexOfReminderTime = CursorUtil.getColumnIndexOrThrow(_cursor, "reminderTime");
          final int _cursorIndexOfNotes = CursorUtil.getColumnIndexOrThrow(_cursor, "notes");
          final List<Habit> _result = new ArrayList<Habit>(_cursor.getCount());
          while(_cursor.moveToNext()) {
            final Habit _item;
            final Long _tmpMyId;
            if (_cursor.isNull(_cursorIndexOfMyId)) {
              _tmpMyId = null;
            } else {
              _tmpMyId = _cursor.getLong(_cursorIndexOfMyId);
            }
            final String _tmpName;
            _tmpName = _cursor.getString(_cursorIndexOfName);
            final int _tmpGoal;
            _tmpGoal = _cursor.getInt(_cursorIndexOfGoal);
            final String _tmpInterval;
            _tmpInterval = _cursor.getString(_cursorIndexOfInterval);
            final int _tmpTimesPerformed;
            _tmpTimesPerformed = _cursor.getInt(_cursorIndexOfTimesPerformed);
            final long _tmpDate_created;
            _tmpDate_created = _cursor.getLong(_cursorIndexOfDateCreated);
            final String _tmpTimerTime;
            _tmpTimerTime = _cursor.getString(_cursorIndexOfTimerTime);
            final String _tmpTimerInterval;
            _tmpTimerInterval = _cursor.getString(_cursorIndexOfTimerInterval);
            final String _tmpReminderTime;
            _tmpReminderTime = _cursor.getString(_cursorIndexOfReminderTime);
            final String _tmpNotes;
            _tmpNotes = _cursor.getString(_cursorIndexOfNotes);
            _item = new Habit(_tmpMyId,_tmpName,_tmpGoal,_tmpInterval,_tmpTimesPerformed,_tmpDate_created,_tmpTimerTime,_tmpTimerInterval,_tmpReminderTime,_tmpNotes);
            _result.add(_item);
          }
          return _result;
        } finally {
          _cursor.close();
          _statement.release();
        }
      }
    }, p0);
  }

  @Override
  public Object getHabit(final String habitName, final Continuation<? super Habit> p1) {
    final String _sql = "SELECT * FROM habit WHERE myId IN (SELECT myId FROM habit WHERE name=?)";
    final RoomSQLiteQuery _statement = RoomSQLiteQuery.acquire(_sql, 1);
    int _argIndex = 1;
    if (habitName == null) {
      _statement.bindNull(_argIndex);
    } else {
      _statement.bindString(_argIndex, habitName);
    }
    return CoroutinesRoom.execute(__db, false, new Callable<Habit>() {
      @Override
      public Habit call() throws Exception {
        final Cursor _cursor = DBUtil.query(__db, _statement, false, null);
        try {
          final int _cursorIndexOfMyId = CursorUtil.getColumnIndexOrThrow(_cursor, "myId");
          final int _cursorIndexOfName = CursorUtil.getColumnIndexOrThrow(_cursor, "name");
          final int _cursorIndexOfGoal = CursorUtil.getColumnIndexOrThrow(_cursor, "goal");
          final int _cursorIndexOfInterval = CursorUtil.getColumnIndexOrThrow(_cursor, "interval");
          final int _cursorIndexOfTimesPerformed = CursorUtil.getColumnIndexOrThrow(_cursor, "timesPerformed");
          final int _cursorIndexOfDateCreated = CursorUtil.getColumnIndexOrThrow(_cursor, "date_created");
          final int _cursorIndexOfTimerTime = CursorUtil.getColumnIndexOrThrow(_cursor, "timerTime");
          final int _cursorIndexOfTimerInterval = CursorUtil.getColumnIndexOrThrow(_cursor, "timerInterval");
          final int _cursorIndexOfReminderTime = CursorUtil.getColumnIndexOrThrow(_cursor, "reminderTime");
          final int _cursorIndexOfNotes = CursorUtil.getColumnIndexOrThrow(_cursor, "notes");
          final Habit _result;
          if(_cursor.moveToFirst()) {
            final Long _tmpMyId;
            if (_cursor.isNull(_cursorIndexOfMyId)) {
              _tmpMyId = null;
            } else {
              _tmpMyId = _cursor.getLong(_cursorIndexOfMyId);
            }
            final String _tmpName;
            _tmpName = _cursor.getString(_cursorIndexOfName);
            final int _tmpGoal;
            _tmpGoal = _cursor.getInt(_cursorIndexOfGoal);
            final String _tmpInterval;
            _tmpInterval = _cursor.getString(_cursorIndexOfInterval);
            final int _tmpTimesPerformed;
            _tmpTimesPerformed = _cursor.getInt(_cursorIndexOfTimesPerformed);
            final long _tmpDate_created;
            _tmpDate_created = _cursor.getLong(_cursorIndexOfDateCreated);
            final String _tmpTimerTime;
            _tmpTimerTime = _cursor.getString(_cursorIndexOfTimerTime);
            final String _tmpTimerInterval;
            _tmpTimerInterval = _cursor.getString(_cursorIndexOfTimerInterval);
            final String _tmpReminderTime;
            _tmpReminderTime = _cursor.getString(_cursorIndexOfReminderTime);
            final String _tmpNotes;
            _tmpNotes = _cursor.getString(_cursorIndexOfNotes);
            _result = new Habit(_tmpMyId,_tmpName,_tmpGoal,_tmpInterval,_tmpTimesPerformed,_tmpDate_created,_tmpTimerTime,_tmpTimerInterval,_tmpReminderTime,_tmpNotes);
          } else {
            _result = null;
          }
          return _result;
        } finally {
          _cursor.close();
          _statement.release();
        }
      }
    }, p1);
  }
}
