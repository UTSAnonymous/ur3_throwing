package ur3_throwing;

public interface ur3_moveRequest extends org.ros.internal.message.Message {
  static final java.lang.String _TYPE = "ur3_throwing/ur3_moveRequest";
  static final java.lang.String _DEFINITION = "float64[6] q\n";
  static final boolean _IS_SERVICE = true;
  static final boolean _IS_ACTION = false;
  double[] getQ();
  void setQ(double[] value);
}
