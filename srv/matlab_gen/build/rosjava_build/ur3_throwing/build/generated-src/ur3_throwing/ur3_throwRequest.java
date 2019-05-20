package ur3_throwing;

public interface ur3_throwRequest extends org.ros.internal.message.Message {
  static final java.lang.String _TYPE = "ur3_throwing/ur3_throwRequest";
  static final java.lang.String _DEFINITION = "bool throw\n";
  static final boolean _IS_SERVICE = true;
  static final boolean _IS_ACTION = false;
  boolean getThrow();
  void setThrow(boolean value);
}
