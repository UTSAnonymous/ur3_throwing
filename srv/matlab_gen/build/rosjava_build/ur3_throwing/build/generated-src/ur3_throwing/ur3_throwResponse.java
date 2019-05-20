package ur3_throwing;

public interface ur3_throwResponse extends org.ros.internal.message.Message {
  static final java.lang.String _TYPE = "ur3_throwing/ur3_throwResponse";
  static final java.lang.String _DEFINITION = "bool Ack";
  static final boolean _IS_SERVICE = true;
  static final boolean _IS_ACTION = false;
  boolean getAck();
  void setAck(boolean value);
}
